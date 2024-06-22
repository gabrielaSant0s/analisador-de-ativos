document.getElementById('ativoForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const ativo = document.getElementById('ativoSelect').value;
    const maiorPreco = document.getElementById('maior-preco').value;
    const menorPreco = document.getElementById('menor-preco').value;
    const volume = document.getElementById('volume').value;
    const periodicidade = document.getElementById('periodicidade').value;

    console.log(email);

    // const cardContainer = document.getElementById('cardsContainer');
    // const card = document.createElement('div');
    // card.className = 'card mb-3';
    // card.innerHTML = `
    //     <div class="card-body">
    //         <h5 class="card-title">${ativo}</h5>
    //         <p class="card-text"><strong>email:</strong> ${email}</p>
    //         <p class="card-text"><strong>Periodicidade:</strong> ${periodicidade}min</p>
    //         <button class="btn btn-warning btn-edit">Editar</button>
    //         <button class="btn btn-danger btn-delete">Excluir</button>
    //     </div>
    // `;

    // cardContainer.appendChild(card);

    // // Limpa o formulário após enviar
    // document.getElementById('ativoForm').reset();

    // // Adiciona funcionalidade aos botões de editar e excluir
    // card.querySelector('.btn-edit').addEventListener('click', function() {
    //     document.getElementById('email').value = email;
    //     document.getElementById('ativo').value = ativo;
    //     document.getElementById('periodicidade').value = periodicidade;
    //     card.remove();
    // });

    // card.querySelector('.btn-delete').addEventListener('click', function() {
    //     card.remove();
    // });
});
