new Vue({
  el: '#app',
  data: {
      mensagem: 'Olá VueJS',
      nome: ''
  },
  methods: {
      mudarNome: function(event) {
          this.nome = event.target.value;
      }
  }
});