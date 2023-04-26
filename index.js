const tmi = require('tmi.js');
const fs = require('fs');
const client = new tmi.Client({
    channels: ['32comma']
});

client.connect();
client.on('message', (channel, tags, message, self) => {
    let content = `${tags['display-name']}: ${message}\n`;
    console.log(content);
    fs.writeFile(`C:\\Workspace\\t20230425\\tts_test\\log\\${new Date().getTime()}.txt`,
        content, { flag: 'a+' }, err => { });
});