// DOM elements
const taskInput = document.getElementById("task-input");
const taskForm = document.getElementById("todo-form");
const taskList = document.getElementById("task-list");

// Task data array
let tasks = [];

// Add event listener to form
taskForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent form submission
    const taskText = taskInput.value.trim();

    if (!taskText) {
        alert("Task cannot be empty!"); // Basic validation
        return;
    }

    addTask(taskText); // Add new task
    taskInput.value = ""; // Clear input field
});

// Add task function
function addTask(taskText, parentIndex = null) {
    try {
        if (typeof taskText !== "string" || !taskText) {
            throw new Error("Task must be a non-empty string.");
        }

        const newTask = { text: taskText, completed: false, subtasks: [] };

        if (parentIndex === null) {
            tasks.push(newTask);
        } else {
            if (!tasks[parentIndex]) throw new Error("Invalid parent index.");
            tasks[parentIndex].subtasks.push(newTask);
        }

        renderTasks();
    } catch (error) {
        alert(error.message);
    }
}

// Render tasks
function renderTasks(taskArray = tasks, parentElement = taskList) {
    parentElement.innerHTML = "";

    taskArray.forEach((task, index) => {
        const taskItem = document.createElement("li");
        taskItem.className = "task";
        if (task.completed) taskItem.classList.add("completed");

        // Apply dynamic styles
        taskItem.style.padding = "10px";
        taskItem.style.margin = "5px 0";
        taskItem.style.border = "1px solid #ddd";
        taskItem.style.borderRadius = "5px";
        taskItem.style.backgroundColor = task.completed ? "#d4edda" : "#f8d7da";

        const taskContent = document.createElement("span");
        taskContent.textContent = task.text;

        const completeButton = document.createElement("button");
        completeButton.textContent = task.completed ? "Undo" : "Complete";
        completeButton.addEventListener("click", () => {
            task.completed = !task.completed;
            renderTasks();
        });

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", () => {
            taskArray.splice(index, 1);
            renderTasks();
        });

        const subtaskButton = document.createElement("button");
        subtaskButton.textContent = "Add Subtask";
        subtaskButton.addEventListener("click", () => {
            const subtaskText = prompt("Enter subtask:");
            if (subtaskText) addTask(subtaskText, index);
        });

        taskItem.appendChild(taskContent);
        taskItem.appendChild(completeButton);
        taskItem.appendChild(deleteButton);
        taskItem.appendChild(subtaskButton);

        parentElement.appendChild(taskItem);

        // Recursively render subtasks
        if (task.subtasks.length > 0) {
            const subtaskList = document.createElement("ul");
            renderTasks(task.subtasks, subtaskList);
            taskItem.appendChild(subtaskList);
        }
    });
}

// Sort tasks function
function sortTasks() {
    tasks = _.sortBy(tasks, "text");
    renderTasks();
}

// Add sort button
const sortButton = document.createElement("button");
sortButton.textContent = "Sort Tasks";
sortButton.addEventListener("click", sortTasks);
document.body.insertBefore(sortButton, taskList);

// Theme toggle
let isDarkTheme = false;

function toggleTheme() {
    isDarkTheme = !isDarkTheme;
    document.body.style.backgroundColor = isDarkTheme ? "#333" : "#fff";
    document.body.style.color = isDarkTheme ? "#fff" : "#000";
}

const themeToggleButton = document.createElement("button");
themeToggleButton.textContent = "Toggle Theme";
themeToggleButton.addEventListener("click", toggleTheme);
document.body.insertBefore(themeToggleButton, document.body.firstChild);
