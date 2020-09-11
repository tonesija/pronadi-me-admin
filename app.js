const readline = require('readline')
const api = require('./api')

const ADMINPW = 'password'


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function sendPost (eggName, eggCode, eggHint) {
    api().post('/createNewEgg', {
        egg: {
                name: eggName,
                password: eggCode,
                hint: eggHint
             },
        password: ADMINPW
    })
    .then(res => console.log('Dodano jaje: ' + res.data.egg.name))
    .catch(err => console.log(err))
}

function sendDelet (eggName) {
    api().post('/deleteEgg', {
        eggName: eggName,
        password: ADMINPW
    })
    .then(res => console.log('Jaje je izbrisano: ' + res.data.eggName))
    .catch(err => console.log(err.response.data.error))
}

let commands = ['create', 'delete']

function split (line) {
    let result = []
    result = line.split(/ +(?=(?:(?:[^"]*"){2})*[^"]*$)/g)
    for(let i = 0; i < result.length; ++i){
        result[i] = result[i].replace(/"/g, '')
    }
    return result
}

function input () {
    rl.question('>', (arg) => {
        let args = split(arg)
        let command = args[0]

        if(commands.includes(command)){
            execute(args)
            input()
        }else {
            console.log('Neispravna naredba.')
            input()
        }
    })
}

function execute (args) {
    switch (args[0]) {
        case 'create':
            if(args.length != 4){
                console.log('Neispravan broj argumenata.')
                break
            }
            sendPost(args[1], args[2], args[3])
            break
        case 'delete':
            if(args.length != 2){
                console.log('Neispravan broj argumenata.')
                break
            }
            sendDelet(args[1])
            break
    }
}

input ()


