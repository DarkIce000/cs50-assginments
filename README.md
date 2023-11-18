# README

# To-Do List With Weather Widget And Inspirational Quotes

This is a chrome Extension that manages your tasks as well as motivating you with a new inspirational quote whenever you open the extension.

## Requirements

1. Latest Chrome
2. Weather API key (if you are seeing this after 30 Nov 2023). Visit https://www.weatherapi.com/ and sign up they will give 15 day trial period.

## Screenshots

![homepage shot.png](README%204f62cb02cce44346a163f28b4dd1c18d/homepage_shot.png)

![1000041262.png](README%204f62cb02cce44346a163f28b4dd1c18d/1000041262.png)

![1000041261.png](README%204f62cb02cce44346a163f28b4dd1c18d/1000041261.png)

## How to Install it ?

1. Go to setting
2. Search extensions
3. Go to extension settings
4. Enable Developer mode
5. Load From Folder
6. Now you are ready to go

## How to Use It ?

1. Pin the extension in tool bar from extension list
2. Now There are already name or location predefined will showing (not to worry). Click the setting On the bottom right corner.
3. From there you are taken to setting page
4. Now fill Your name and Location

> Note : Location should be city name or {longitude} / {latitude} format only, Zipcode is supported only for USA.
>
1. Click on save. Done. Go back by click on the top.

## How things works ?

### To-Do functionality:

1. You can create a task by entering the task and then adding.
2. You can mark it as completed and it turn into green and striked through.
3. You can remove it by clicking on the cross icon on the right side of each task
4. It can retain the previous added tasks by storing it in the user browser on reopening or reloading or even restarting the browser.

### Weather Showing:

1. All the data of the current weather is coming directly from the weather api used i.e https://weatherapi.com
2. Icon of the Weather showing is also come from the from api
3. So those are all dynamics
4. Location of the Weather showing below is the location entered by the user or default location.
5. This can be changed in the Setting Page

### Greeting:

1. Name can be changed in the setting page

### Digital Clock:

1. This cannot be Changed in the setting if you wish you can change in the JS file.



## Now let see What I have in my JS file

I have two files of javascript 1st in which Most of the functionality has been added
and second is for Setting page

### script.js
    ---
    On the top you will see this code:


    `//this is the counter variable for the number of tasks added
        let count = 0;
        let tasklist = document.getElementById('tasklist');


        //load the tasks
        function loadPreviousSessionTasks(){
            //username of the user
            const username =  document.getElementById('Username');
            username.innerText  = localStorage.getItem('username');

            let loadSession = localStorage.getItem('savedData');
            if (loadSession){
                //displaying on the page
            tasklist.innerHTML = loadSession;
            }
        }

        function saveData(){
            let task = tasklist.innerHTML;
            localStorage.setItem('savedData', task);
        }



        //to do list functionality
        document.addEventListener('DOMContentLoaded', () => {

            loadPreviousSessionTasks();

            document.querySelector('form').onsubmit = () => {
                const inputTask = document.querySelector('form')

                if (inputTask.value === ''){
                    alert('write something')
                    return false;
                }
                else{
                    const task = document.querySelector('#task');
                    const li = document.createElement('li');
                    li.className = "list-group-item"
                    li.innerHTML = task.value;

                    const span = document.createElement('span');
                    span.innerHTML = '\u00d7';

                    //show on the Html document page
                    document.querySelector('#tasklist').append(li);
                    li.appendChild(span);

                    //save to local storage
                    saveData();


                    //clear input field
                    task.value = '';

                    //stop form from submitting
                    return false;

                }
        };
        });

        //removing of task and strike though when marked as checkd
        tasklist.addEventListener('click', function(event){
            if( event.target.tagName === "LI"){
                event.target.classList.toggle("checked");
                saveData();
            }
            else if(event.target.tagName === "SPAN"){
                event.target.parentElement.remove();
                saveData();
            }
        }, false)
        `
>which is used in creating the todo functionality of the app.


Now let move to the another block which feature the Digital Clock:

`
///digital clock showing onthe page
function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);

    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    document.getElementById('date').innerHTML =  h + ":" + m + ":" + s;

    setTimeout(startTime, 1000);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
};

document.addEventListener('DOMContentLoaded', startTime);
`

> this block of code add a digital clock in the extension page


Moving forward:

`/tips showing code

function randomTips(){
    const tips = {"Mahatma Gandhi":"Learn as if you will live forever, live like you will die tomorrow.",
    "Eleanor Roosevelt": "When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.",
    "Diane McLaren": "It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest.",
    "Herman Malville": "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Henry David Thoreau": "Success usually comes to those who are too busy looking for it.",
    "Tony Robbins": "Setting goals is the first step in turning the invisible into the visible.",
    "John Wooden": "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable",
    "W. P. Kinsella": "Success is getting what you want, happiness is wanting what you get."
    }

    const header = Object.keys(tips)
    const lengthHeader = header.length
    //chosing a random index
    const randomH = Math.ceil(Math.random()*lengthHeader) - 1
    console.log(randomH);
    //accesing that index content
    const tipBody = tips[header[randomH]]
    const tipHead = header[randomH]

    //creating object for returning the tips
    let tip = {};
    tip[tipHead] = tipBody;
    return tip
};

document.addEventListener('DOMContentLoaded', function(){
    const cardTitle = document.querySelector('.card-title')
    const cardText = document.querySelector('.card-text')
    const tip = randomTips()
    cardTitle.innerText = Object.keys(tip)[0]
    cardText.innerText = tip[Object.keys(tip)[0]]
});

`

> this block of code show inspirational quotes from a list of quotes that i have taken from the internet

Next,

`//weather showing on the page using weatherapi if this does not working that likely means you are seeing the code
//after 30th nov 2023. this is my end of the trial period date of that weather api if you want to revive this feature again
//go to search weatherapi.com on google sign in then they will give you an api key just replace after key= {your apikey}
//but till before

document.addEventListener('DOMContentLoaded', function(){

    const savedLocation = localStorage.getItem('location');

    fetch(`http://api.weatherapi.com/v1/current.json?key=53024ea6362d4014a7124444231611&q=${savedLocation}&aqi=no`)
    .then(response => response.json())
    .then( data => {
        //temperature display as text
        const temp = document.querySelector('#temp')
        temp.innerText = data.current.temp_c

        const tempIcon = document.querySelector('#weather-condition-icon')
        tempIcon.src = 'https:'+ data.current.condition.icon

        //location showing
        const location = document.querySelector('#location')
        location.innerText = data.location.name + ", " +data.location.region + ", " + `(${data.location.country})`

        console.log(data)
        console.log(data.current.temp_c)
        console.log('https:'+ data.current.condition.icon)
    });
});
`
>Next and Last is this Line of code which get the temperature and weather data from weatherapi and show on the chrome extension. This is the main 2nd main feature of the extension.

