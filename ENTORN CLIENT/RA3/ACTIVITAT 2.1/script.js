let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

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

    // Afegir nova tasca
    tasks.push({
        id: Date.now(),
        text: text,
        completed: false
    });

    // Guardar al LocalStorage
    saveTasks();
    
    // Actualitza la pantalla
    displayTasks();
    
    // Netejar input
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
        <li class="${task.completed ? 'completed' : ''}" ondblclick="toggleTask(${task.id})">
            <span class="task-text">${task.text}</span>
            <div>
                <button class="delete-btn" onclick="deleteTask(${task.id})">🗑️</button>
            </div>
        </li>
    `).join('');
}
