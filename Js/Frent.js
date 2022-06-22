const tabela = document.querySelector('.corpo-tabela');
const botaoAtualizar = document.querySelector('.botao-atualizar');

pegarDados();

botaoAtualizar.addEventListener('click', pegarDados);

function pegarDados() {
  fetch("http://127.0.0.1:5000")
  .then(function (dados) {
    return dados.json();
  })
  .then(function (board) {
    popularTabela(board);
  });
}

function popularTabela(dados) {
  tabela.innerHTML = '';
  for(let index = 0; index < dados.length; index++) {
    const tr = document.createElement('tr');
    const colunaNome = document.createElement('td');
    const colunaIdade = document.createElement('td');
    const colunaTipo = document.createElement('td');
    const colunaValor = document.createElement('td');

    colunaId.innerHTML = dados[index]['_id'];
    colunaNome.innerHTML = dados[index]['board'];


    tr.appendChild(colunaId);
    tr.appendChild(colunaNome);

    tabela.appendChild(tr);
  }
}