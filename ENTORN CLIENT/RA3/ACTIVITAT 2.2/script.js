let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Afegeix comptador i assegura que completed estigui desactivat (compatibilitat versions anteriors)
tasks = tasks.map(task => ({
    ...task,
    completed: false,
    count: typeof task.count === 'number' ? task.count : 1
}));

// Carrega les tasques al inici
displayTasks();

// Event listeners
document.getElementById('addBtn').addEventListener('click', addTask);
document.getElementById('taskInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});

function addTask() {
    const input = document.getElementById('taskInput');
    const text = input.value.trim();

    if (text === '') {
        alert('Escriu una tasca!');
        return;
    }

    const duplicate = tasks.some(task => task.text.toLowerCase() === text.toLowerCase());
    if (duplicate) {
        alert('Aquesta tasca ja existeix!');
        return;
    }

    // Afegir nova tasca
    tasks.push({
        id: Date.now(),
        text: text,
        completed: false,
        count: 1
    });

    saveTasks();
    displayTasks();
    input.value = '';
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    displayTasks();
}

function toggleTask(id) {
    const task = tasks.find(t => t.id === id);
    if (task) {
        task.completed = !task.completed;
        saveTasks();
        displayTasks();
    }
}

function incrementCount(id) {
    const task = tasks.find(t => t.id === id);
    if (task) {
        task.count += 1;
        saveTasks();
        displayTasks();
    }
}

function decrementCount(id) {
    const task = tasks.find(t => t.id === id);
    if (task && task.count > 0) {
        task.count -= 1;
        saveTasks();
        displayTasks();
    }
}

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Mostra les tasques a la pantalla
function displayTasks() {
    const taskList = document.getElementById('taskList');
    
    if (tasks.length === 0) {
        taskList.innerHTML = '<li class="empty">No tens tasques pendents!</li>';
        return;
    }

    taskList.innerHTML = tasks.map(task => `
        <li class="${task.completed ? 'completed' : ''}">
            <div class="task-main">
                <span class="task-text">${task.text}</span>
                <div class="counter">
                    <button class="counter-btn" onclick="decrementCount(${task.id}); event.stopPropagation();">-</button>
                    <span class="count">${task.count}</span>
                    <button class="counter-btn" onclick="incrementCount(${task.id}); event.stopPropagation();">+</button>
                </div>
            </div>
            <div class="actions">
                <button class="delete-btn" onclick="deleteTask(${task.id}); event.stopPropagation();">🗑️</button>
            </div>
        </li>
    `).join('');
}
