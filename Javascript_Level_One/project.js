var firstName = prompt("Hello and Welcome. Please enter your first name:");
var lastName = prompt("Please enter your Last Name");
var age = prompt("What is your Age?");
var height = prompt("How tall are you in centimeters");
var petName = prompt("What is the name of your pet?");
alert("Thank you so much for the information");

if((firstName[0] == lastName[0]) && age>20 && age<30 && height >=170 && petName[petName.length-1]=="y")
{
  console.log("Welcome Comrade! You've Passed the Spy Test");
}
else {
  console.log("Sorry, there is nothing to see!!!");
}
