import jsonfile from 'jsonfile';
import moment from 'moment';
import simpleGit from 'simple-git';
import random from 'random';

const FILE_PATH = './data.json';

const makeCommit = n => {
  if (n === 0) return simpleGit().push();

  const x = random.int(0, 54);
  const y = random.int(0, 6);
  const DATE = moment().subtract(1, 'y').add(1, 'd').add(x, 'w').add(y, 'd').format();
  
  const data = {
    date: DATE
  };

  console.log(`Committing for date: ${DATE}`);

  jsonfile.writeFile(FILE_PATH, data, (err) => {
    if (err) {
      console.error('Error writing JSON:', err);
      return;
    }

    console.log(`Successfully wrote to ${FILE_PATH}`);
    
    simpleGit().add([FILE_PATH]).commit(DATE, { '--date': DATE }, (err) => {
      if (err) {
        console.error('Commit failed:', err);
        return;
      }
      
      console.log(`Committed with date: ${DATE}`);
      
      // Push changes after commit
      simpleGit().push((err) => {
        if (err) {
          console.error('Push failed:', err);
          return;
        }
        
        console.log('Pushed to remote repository');
        // Recursive call to make more commits
        makeCommit(--n);
      });
    });
  });
};

makeCommit(100);
