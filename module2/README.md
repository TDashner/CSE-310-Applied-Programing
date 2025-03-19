# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}

I made a Peer-to-Peer Chat Application that allows two peers to communicate by sending and receiving messages simultaneously. The purpose of learning this module for myself is to better help my websites maintain optimization for clients to contact me or the company on the site for any troubleshooting that may occur.

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}

peer-to-peer

{Identify if you are using TCP or UDP and what port numbers are used.}

UDP

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

# Development Environment

{Describe the tools that you used to develop the software}
First, you need to install the library cryptography. Then, you need to have two different computers (for the best demonstration) or install a virtual machine running Linux. If it's running on two different computers, you need to find the local IP address of each device through ipconfig in a command prompt. You would start the code on both computers and enter their own ports and the IP address of the other peer. If you have it running on the same computer, you should open two seperate terminal windows and use 127.0.0.1 for the IP, but different ports. 

{Describe the programming language that you used and any libraries.}

This is made through python and I used the libraries socket, threading, tkinter, and Fernet from cryptography.fernet

I had issues with receiving messages at first
I also needed to increase the buffer size
The message's signature wasn't matching up with the expected one, so the Fernat key wasn't being used in the same way for both encrypting and decrypting messages

For the stretch challenge, I had my program provide a graphical user interface (GUI) for your program instead of the command line.

When you press the "Change Encryption Key" button:
The key is changed, and the cipher object is updated.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Youtube](https://www.youtube.com/watch?v=VKSlacce9QQ): An example of a peer to peer python module
* [Chatgpt](https://chatgpt.com/): This was used for error handling and helped tell me what the errors meant
* [W3Schools](https://www.w3schools.com/cybersecurity/cybersecurity_networking.php): Networking basics


# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
Make the name display possibly all uppercase (and it works)
* Item 2
Make it more enticing to look at. Maybe add some css to it later on
* Item 3
