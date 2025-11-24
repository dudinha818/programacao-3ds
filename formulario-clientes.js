0 unsaved changes 

HTML Options
27
  
28
      db.run(`INSERT INTO Clientes (Id, Nome, Email) VALUES (2, 'Bruno', 'bruno@email.com');`);
29
      db.run(`INSERT INTO Clientes (Id, Nome, Email) VALUES (3, 'Rose', 'rose@email.com');`);
30
​
31
​
32
    function buscarCliente() {
33
      const id = document.getElementById('idBuscar').value;
34
      const stmt = db.prepare("SELECT * FROM Clientes WHERE Id = ?");
35
      stmt.bind([id]);
36
      let result = '';
37
      while (stmt.step()) {
38
        const row = stmt.getAsObject();
39
        result = `Nome: ${row.Nome}, Email: ${row.Email}`;
40
      }
41
      stmt.free();
42
      document.getElementById('resultado').innerText = result || 'Cliente não encontrado.';
43
    }
44
​
45
    function excluirCliente() {
46
      const id = document.getElementById('idExcluir').value;
47
      db.run("DELETE FROM Clientes WHERE Id = ?", [id]);
48
      document.getElementById('exclusao').innerText = 'Cliente excluído com sucesso!';
49
    }
50
  </script>
51
</body>
52
</html>
53
​
