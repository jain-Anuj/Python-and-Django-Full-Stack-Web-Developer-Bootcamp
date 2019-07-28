var arr = [];
function roaster(){
  var startChoice = prompt("Would you like to start the roster web app?(y/n)");
  if(startChoice == "y")
  {

    var taskChoice = null;
    do {
      taskChoice = prompt("Please select an action: add, remove, display or quit.");
      if(taskChoice == "add"){
        var name = prompt("What name would you like to add?");
        add(name);
      }
      else if (taskChoice == "remove") {
        var name = prompt("What name you want to remove?");
        remove(name);
      }
      else if(taskChoice == "display")
      {
        display();
      }
    } while (taskChoice != "quit");
    alert("Thank you for using the roaster web app!!")
  }
  else{
    alert("Fuck Off!!")
  }
}

function add(name)
{
  arr.push(name);
}

function remove(name){
  var index = arr.indexOf(name);
  if(index > -1){
    arr.splice(index,1);
  }
}

function display()
{
  console.log(arr);
}

roaster();
