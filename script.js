
/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }
*/

const GIF = document.getElementById("loader");
async function fetchData() {
  const response = await fetch("http://localhost:8000/menu").then(
    async (response) => {
      GIF.style.display = "none";
        const data = await response.json();
        console.log(data);
        addFetchData(data['items']);
});}

function addFetchData(items) {
  makeNewDiv(items,"chum_burger")
  makeNewDiv(items,"kelp_fries")
  makeNewDiv(items,"krabby_patty")
  makeNewDiv(items,"krusty_krab_pizza")
}

function makeNewDiv(items,nameOfObj){
  const menu = document.getElementById("menu");
  const div = document.createElement("div");
  const h = document.createElement("h3");
  const p = document.createElement("p");
  const input = document.createElement("input");

  description = items[nameOfObj].description;
  Name = items[nameOfObj].name;
  price = items[nameOfObj].price;
  h.textContent = `${Name} ($ ${price})`
  p.textContent = description;
  input.setAttribute("type","number")
  input.setAttribute("value",0)
  input.setAttribute("min",0)
  input.setAttribute("max",5)

  div.classList.add("card");
  div.appendChild(h)
  div.appendChild(p)
  div.append(input)
  menu.appendChild(div)
}

fetchData();


