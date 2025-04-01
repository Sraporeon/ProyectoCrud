let records = [];
let idCounter = 1;

const form = document.getElementById('crud-form');
const recordsTable = document.getElementById('records-table').getElementsByTagName('tbody')[0];

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.name.value.trim();
    const description = form.description.value.trim();

    if (name && description) {
        const record = { id: idCounter++, name, description };
        records.push(record);
        form.reset();
        renderTable();
    }
});

function renderTable() {
    recordsTable.innerHTML = '';

    records.forEach(record => {
        const row = recordsTable.insertRow();

        row.innerHTML = `
            <td>${record.id}</td>
            <td>${record.name}</td>
            <td>${record.description}</td>
            <td>
                <button onclick="editRecord(${record.id})">Edit</button>
                <button onclick="deleteRecord(${record.id})">Delete</button>
            </td>
        `;
    });
}

function editRecord(id) {
    const record = records.find(r => r.id === id);
    if (record) {
        form.name.value = record.name;
        form.description.value = record.description;

        deleteRecord(id); 
    }
}

function deleteRecord(id) {
    records = records.filter(record => record.id !== id);
    renderTable();
}

renderTable();
