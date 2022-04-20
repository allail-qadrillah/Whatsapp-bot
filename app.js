const { Client, LegacySessionAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode');
const express = require('express');
const socketIO = require('socket.io');
const http = require('http');

const fs = require('fs');
const { url } = require('inspector');
const  rmeme  =  require('rmeme');
const mime = require('mime-types');
const port = process.env.PORT || 8000;

const App = express();
const server = http.createServer(App);
const io = socketIO(server);


App.set("port", process.env.PORT || 5000);

const getBreeds = async () => {
    const browserP = await puppeteer.launch({
    args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
    ],
    });}

console.log("1")

App.get('/', (req, res) => {
    res.sendFile('index.html', {root: __dirname})
})
App.get('/main', function (req, res) {
  res.send('GET request to homepage')
  client.on('qr', (qr) => {
    // Generate and scan this code with your phone
    console.log('QR RECEIVED', qr);
});
})

// AUTENTIKASI QR CODE
// Path where the session data will be stored
const SESSION_FILE_PATH = './session.json';
// Load the session data if it has been previously saved
let sessionData;
if(fs.existsSync(SESSION_FILE_PATH)) {
    sessionData = require(SESSION_FILE_PATH);
}
console.log("2")

// Use the saved values
const client = new Client({
    authStrategy: new LegacySessionAuth({
        session: sessionData
    })
});
client.on('qr', (qr) => {
    // Generate and scan this code with your phone
    console.log('QR', qr);
});
// Save session values to the file upon successful auth
client.on('authenticated', (session) => {
    sessionData = session;
    fs.writeFile(SESSION_FILE_PATH, JSON.stringify(session), (err) => {
        if (err) {
            console.error(err);
        }
    });
});

console.log("3")

// RECEIVE MESSAGE
client.on('message', async msg => {
    if (msg.body == 'salamm') {
        console.log(msg.body);
        msg.reply('salam balikkkkkk!');
    }

    // HANDLE PESAN -meme
    else if (msg.body == '-meme') { 
        const IMGurl  = await rmeme.meme(); // dapatkan link gambar
        const media = await MessageMedia.fromUrl(IMGurl); // dapatkan gambar
        await client.sendMessage(msg['_data']['from'], media) // kirim gambar
    
    // HANDLE IMAGE AND SEND STICKER
    }else if (msg.hasMedia){
        msg.downloadMedia().then( media =>{
            if(media){
                
                const mediaPath = './downloaded-media'
                if(!fs.existsSync(mediaPath)){
                    fs.mkdirSync(mediaPath)

                }
                // buat nama dan tipe file
                const exstension   = mime.extension(media.mimetype);
                const fileName     = new Date().getTime();
                const fullFileName = mediaPath+ '/' + fileName + '.' + exstension;

                // Save File
                try{
                    // download gambar jadi sticker
                    fs.writeFileSync(fullFileName, media.data, {encoding : 'base64'});
                    console.log("File Downloaded", fullFileName);
                    MessageMedia.fromFilePath(filePath = fullFileName);
                    // kirim sticker
                    client.sendMessage(msg['_data']['from'], new MessageMedia(media.mimetype, media.data, fileName), 
                    {sendMediaAsSticker:true, stickerAuthor:"Created by Bot", stickerName:"Stickers"});
                    // fs.unlinkSync(fullFileName); // hapus file

                } catch(err){
                    msg.reply('tidak dapat mengubahnya jadi sticker :"');
                    console.log("Failed Downloaded File", err);
                }
            }   
        })
    }
});


// Socket IO
io.on("connection", function(socket) {
    socket.emit('message', 'Connecting.....');
    console.log("4")
    client.on('qr', (qr) => {
        console.log("mendapatkan qrcode")
        // Generate and scan this code with your phone
        console.log('QR RECEIVED', qr);
        qrcode.toDataURL(qr, (err, url) => {
            socket.emit('qr', url)
            socket.emit('message', "QR Code Received")
        }) 
        console.log("5")
    });
    
    client.on('ready', () => {
        socket.emit('message', "WhatsApp is Ready!")
    });
})

server.listen(port, function() { 
  console.log("App runningg on port", port)
});

// // npm ERR! Missing: http@0.0.1-security from lock fil 
// // remote:        npm ERR! Missing: qrcode@1.5.0 from lock file       
// // remote:        npm ERR! Missing: rmeme@1.1.0 from lock file        
// // remote:        npm ERR! Missing: socket.io@4.4.1 from lock file    
// // remote:        npm ERR! Missing: supervisor@0.12.0 from lock file  
// // remote:        npm ERR! Missing: whatsApp-web.js@1.16.

// console.log('Start')
// const { Client } = require('whatsapp-web.js');

// const getBreeds = async () => {
//     const BrowserRunner = await puppeteer.launch({
//     args: [
//         '--no-sandbox',
//         '--disable-setuid-sandbox',
//     ],
//     });}

// const client = new Client();

// console.log('getting qr code')
// client.on('qr', (qr) => {
//     // Generate and scan this code with your phone
//     console.log('QR RECEIVED', qr);
// });

// console.log("yey")

// client.on('ready', () => {
//     console.log('Client is ready!');
// });

// client.on('message', msg => {
//     if (msg.body == '!ping') {
//         msg.reply('pong');
//     }
// });

// client.initialize();