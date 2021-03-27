const fs = require('fs');
const readline = require('readline');
const {google} = require('googleapis');


const readlineSync = require('readline-sync');
const { parse } = require('path');

const chalk = require('chalk');
 

var userName = readlineSync.question(chalk.green('May I have your name? \n\n'));
console.log(chalk.blueBright('Hi ' + chalk.yellow.bold(userName) + '!\n\n\n'));
console.log(chalk.yellowBright("Welcome to sekureMail,\nHere you can automatically delete unwanted or spam mail sent to you through keywords, sender mail ID, or for attachments.\nNOTE! : Set only the keywords, mail Id or attachment which you seems to be a spam.\n\n\n"));



const SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic'];
const TOKEN_PATH = 'token.json';


fs.readFile('credentials.json', (err, content) => {
  if (err) return console.log('Error loading client secret file:', err);
  authorize(JSON.parse(content), createFilter);
});

function authorize(credentials, callback) {
  const {client_secret, client_id, redirect_uris} = credentials.installed;
  const oAuth2Client = new google.auth.OAuth2(
      client_id, client_secret, redirect_uris[0]);

  fs.readFile(TOKEN_PATH, (err, token) => {
    if (err) return getNewToken(oAuth2Client, callback);
    oAuth2Client.setCredentials(JSON.parse(token));
    callback(oAuth2Client);
  });
}

function getNewToken(oAuth2Client, callback) {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: SCOPES,
  });
  console.log('Authorize this app by visiting this url:', authUrl);
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.question('Enter the code from that page here: ', (code) => {
    rl.close();
    oAuth2Client.getToken(code, (err, token) => {
      if (err) return console.error('Error retrieving access token', err);
      oAuth2Client.setCredentials(token);
      fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
        if (err) return console.error(err);
        console.log('Token stored to', TOKEN_PATH);
      });
      callback(oAuth2Client);
    });
  });
}

function createFilter(auth){
    var gmail = google.gmail('v1');
    let firstQ = readlineSync.keyIn(chalk.greenBright("How do you want to filter your mail from:\n(a.) Sender\n(b.) A Keyword\n(c.) Attachment\nType the option key:\n\n"),{limit: '$<a-c>'});
    let fillKey = "";
    let irrMail = "";
    firstQ = firstQ.toLowerCase();

    if (firstQ == "a"){
        fillKey = "from";
        irrMail = readlineSync.questionEMail(chalk.greenBright("Type that spam mail here: "));
    }
    else if(firstQ == "b"){
        fillKey = "query";
        irrMail = readlineSync.question(chalk.greenBright("Any suspicious keyword which you don't want from the mail : "));
    }
    else if(firstQ == "c"){
        fillKey = "hasAttachment"
        irrMail = "true";
    }
    const data = {
        criteria: {
            [fillKey] : `${irrMail}`,
        },
        action: {
            addLabelIds: [
                "TRASH",
            ],
        },
    };
    
    gmail.users.settings.filters.create({
      auth: auth,
      userId: 'me',
      resource: data,
    }, function(err, result) {
      if (err) {
        console.log(chalk.redBright("\n\nYour filter has already been created!\n\n"));
      } else {
        console.log(chalk.yellowBright(`\n\nCongrats! Your filter is just created.\n\n`));
        callback( result );
      }
    });
  }
