def submit_data(data, client, address):
  client.connect(address)
  client.senr(data.encode())