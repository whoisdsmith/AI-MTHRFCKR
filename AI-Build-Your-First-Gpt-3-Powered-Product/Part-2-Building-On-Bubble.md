# Part 2: Building on Bubble

Files & media: 122.Idea_18.png

We will create a simple one-page application on Bubble that takes the response and gives an output using the OpenAI API.

## 1. Creating the Page

- Once you have created an account and created your first app, you will see the Bubble application design window.
- Click on Page > Add New Page > Name the page > Create
- Add a Group for the inputs
- Add a Multiline Input > Double click > Layout > Uncheck Fixed Width > Customise the height as you want
- Add a Text above > Double click > Appearance > Add the text that you want to appear
- Add all the input fields we want
- Add a button > Layout > Uncheck Fixed Width > Appearance > Add the text and change colour as desired
- Select the group > Layout > Max Width 640 & center aligned

<aside>
⚠️ Tip: You can add space between the elements with Margins under Layout

</aside>

Great, the inputs are ready. The result will display below the button. So let’s create the Output

- Add a Text > Give it a heading
- Add Another text below. This will be the element where we will display the response.

[Part 1.mp4](Part%202%20Building%20on%20Bubble%20af5b16ba2e834080aa37fc1bc0d4d5a1/Part_1.mp4)

## 2. Connecting to OpenAI API

- Click on Plugins > Add New Plugin > API Connector > Install
- Give a name > Add API Call > Name > Expand
- Go to OpenAI Playground and click View Code > Curl
- On Bubble, select POST and add the first link from the code

![Screen Shot 2023-01-29 at 9.31.17 PM.png](Part%202%20Building%20on%20Bubble%20af5b16ba2e834080aa37fc1bc0d4d5a1/Screen_Shot_2023-01-29_at_9.31.17_PM.png)

- Click Add Header > Add Content type & Authorization headers from the code

![Screen Shot 2023-01-29 at 9.45.40 PM.png](Part%202%20Building%20on%20Bubble%20af5b16ba2e834080aa37fc1bc0d4d5a1/Screen_Shot_2023-01-29_at_9.45.40_PM.png)

- For the Authorization header, you will need to add your OpenAI API key
    - Account > API Keys > Create a new secret key
- Change the code to JSON in OpenAI
- Copy and paste on the Bubble in the body
- Bubble allows sending of dynamic data in the API call. We will modify the prompt with input data.
- In the body code, wherever you want a dynamic field, add <>

![Screen Shot 2023-01-29 at 9.34.42 PM.png](Part%202%20Building%20on%20Bubble%20af5b16ba2e834080aa37fc1bc0d4d5a1/Screen_Shot_2023-01-29_at_9.34.42_PM.png)

- Uncheck Private for each parameter
- Check Capture response headers
- Click Initialize call
- In the pop-up, Click Show Raw Data.
- The text will have the output
- Note down word before the text

[Part 2.mp4](Part%202%20Building%20on%20Bubble%20af5b16ba2e834080aa37fc1bc0d4d5a1/Part_2.mp4)

## 3. Connect the API to the Interface

- On the design page on Bubble, Double click the button > Start Workflow
- Click to Add Actions > Plugins > OpenAI
- Match each Parameter to the Input fields
- Add another action > Element Actions > Set State
- Select the page as the Element > Custom State Create > Name > Text
- Value > Result of Step 1 > Body > Choices > First Item
    - Remember the word we noted down at the end of API that we will use to connect the response here
- Go back to the Design page
- Double click the text where we want the response > Add Dynamic text > Page’s state that we created

[Part 3.mp4](Part%202%20Building%20on%20Bubble%20af5b16ba2e834080aa37fc1bc0d4d5a1/Part_3.mp4)

Your App is ready for use!

![https://media.giphy.com/media/WYyvz9PIhjLHgiyvR2/giphy.gif](https://media.giphy.com/media/WYyvz9PIhjLHgiyvR2/giphy.gif)