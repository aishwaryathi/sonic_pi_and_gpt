<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Musical Chatbot for Sonic Pi Powered through GPT</title>
  </head>
  <body>
    <header>
      <h1>Video Demo: https://youtu.be/tPoTf8IxrQ0 </h1>
      <h1>Musical Chatbot for Sonic Pi Powered through GPT</h1>
    </header>
    <section>
      <h2>Project Introduction</h2>
      <p>
        Throughout this course, my favorite lesson was learning about live
        coding with Sonic Pi. Especially when I was practicing for the live
        coding sessions, I would frequently use ChatGPT to guide me through
        creating different Live Loops or creative Melodies. Therefore, I
        originally proposed to create some kind of project that formally
        incorporates GPT and Sonic Pi. Through planning this project, I decided
        that it would be best to use a python interpreter tool, namely “musical
        chatbot.”
      </p>
      <h2>Integration Challenges and Alternatives</h2>
      <p>
        Ideally, my vision for the "musical chatbot" was to have it integrated
        as a direct extension within Sonic Pi, allowing users to interact with
        the chatbot in a integrated environment. This integration would have
        provided a more intuitive user experience by eliminating the need to
        switch between different applications or interfaces. However, this
        direct integration poses significant technical challenges and
        limitations at present. Specifically, Sonic Pi doesn’t currently allow
        adding or creating extensions on top of the application.
      </p>
      <p>
        As a result, I had to explore alternative ways to incorporate the
        functionality of the chatbot. The solution I settled on involves using a
        standalone Python interpreter tool to manage the chatbot functionality.
        This approach requires users to operate through their terminal to
        interact with the "musical chatbot". While this method introduces an
        additional step for users, it still effectively allows for the
        communication between the user, the chatbot, and Sonic Pi through socket
        programming and invoking openAI API. This setup, although not as
        streamlined as a direct integration, provides a functional workaround
        that maintains the project's objectives of interactive musical creation
        using AI guidance.
      </p>
      <h2>Communication Goals</h2>
      <p>
        In my project, my main goal was to incorporate two goals: use sockets
        programming to communicate between my interpreter tool, and utilize the
        OpenAI API in order to get access to ChatGPT. I was able to get access
        to OpenAI API by retrieving an api key designated for GPT modelling.
        Then, I incorporated that key in my python script so that I can use that
        key to call the OpenAI API.
      </p>
    </section>
    <section>
      <h2>Mode Descriptions</h2>
      <p>
        In my project, I wanted to give the user a variety of options and
        versatility. Thus I created three options: simple, intermediate, and
        hard mode. Along these modes/methods, I also incorporated an additional
        method in case the user has general questions.
      </p>
      <h2>Simple Mode</h2>
      <p>
        In Simple Mode, I focused on utilizing socket programming to facilitate
        direct communication with Sonic Pi. Initially, I encountered challenges
        in managing long and complicated live loops via sockets. To simplify
        this, I limited the user’s choices to 16 distinct samples, which proved
        to be more manageable. Here, users can select a sample and specify a
        sleep time to control the pause between the loops. I then take both
        pieces of information and send them through a UDP client socket to Sonic
        Pi.
      </p>
      <p>
        The process is interactive but requires some manual work from the user.
        After choosing their settings, users need to copy and paste the
        generated loop into Sonic Pi themselves. This loop integrates the
        selected sample and sleep time to create a simple live loop, which the
        user can then modify or expand upon. This mode offers a hands-on
        approach to experimenting with different samples and sleep durations,
        allowing users to actively engage with music creation. Here’s a quick
        rundown of how I set it up:
      </p>
      <p>
        I start by displaying the 16 sample options, and the user selects one by
        entering its corresponding number. I make sure the input is valid—a
        number between 1 and 16. Next, the user specifies the sleep time in
        half-second increments, up to a maximum of five seconds, ensuring this
        input is within the defined range. After receiving these inputs, I open
        Sonic Pi on the user’s machine and, if confirmed by the user, send the
        details directly to Sonic Pi to start the loop. If the user wants to try
        different settings, they can easily restart this process, or they can
        choose to exit after their session. This simple mode aims to introduce
        users to the basics of live coding with a straightforward, interactive
        setup that emphasizes learning and exploration.
      </p>
      <h2>Intermediate Mode</h2>
      <p>
        In the intermediate mode, my project really comes into action with the
        integration of ChatGPT, powered by OpenAI's API—specifically the
        4.0-turbo model. Here, I implemented the strategy outlined in my
        proposal, where ChatGPT generates a selection of options in three key
        categories crucial for composing music: mood, genre, and instrument.
      </p>
      <p>
        I designed the system to present users with five options in each
        category, generated randomly by the AI. Users then select their
        preferred option from each category, making their choices based on
        personal taste or the specific requirements of the music piece they
        envision. This interactive selection process is to basically create a
        personalized music composition experience.
      </p>
      <p>
        After the selections are made, I take these choices and feed them back
        into the API, requesting it to generate a Sonic Pi melody that embodies
        the chosen theme. Initially, my plan was to streamline this process
        using socket communication to send the GPT-generated code directly to
        Sonic Pi. However, I soon realized that transferring large blocks of
        code this way was impractical—it would necessitate extensive additional
        coding on the Sonic Pi side and potentially lead to errors and
        confusion.
      </p>
      <p>
        To simplify the user experience and ensure robust functionality, I
        decided to save the generated code into a Ruby file (specifically named
        “sonic_pi_code.rb”). This approach not only preserves the integrity of
        the code but also makes it easily accessible and modifiable by the user.
        After saving the file, I automate the process of opening both Sonic Pi
        and the newly created file, setting everything up for the user to start
        experimenting right away.
      </p>
      <h2>Hard Mode</h2>
      <p>
        In hard mode, the user can ask musical chatbot (which then invokes
        openAI API to use GPT) to create a Sonic Pi melody based on their own
        instructions. Users begin by providing an instruction, like "recreate
        the song Billie Jean by Michael Jackson." I then send this input to the
        OpenAI API, prompting it to generate a Sonic Pi melody that abides by
        the instruction using existing Sonic Pi features.
      </p>
      <p>
        Once the melody is generated and presented to the user, I offer the
        option to modify it. If the user wants changes, they provide additional
        instructions, and I use ChatGPT again to adjust the melody based on this
        new input. The updated version is then shown to the user. Then, I use
        the python interpretor tool to directly open the file (with the
        generated response) and open Sonic Pi through the
        save_and_open_in_sonic_pi() method.
      </p>
      <p>
        This process continues iteratively—generation, presentation,
        modification—until the user is satisfied or chooses not to make further
        changes. At this point, I transition to a general Q&A to address any
        other questions the user might have.
      </p>
      <h2>Saving and Opening in Sonic Pi</h2>
      <p>
        While it was difficult to send large blocks of text through osc
        listeners in Sonic Pi, I still wanted the user that have some ease with
        transporting their generated code onto Sonic Pi. Therefore, this method
        handles the generated Sonic Pi code, saves it to a specified file, and
        then automatically opens both the file and Sonic Pi application on the
        user's system.
      </p>
    </section>
  </body>
</html>
