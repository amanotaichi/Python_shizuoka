const pokedexUser = document.getElementsByClassName("pokedex")[0];
const pokedexCpu = document.getElementsByClassName("pokedex")[1];
const randomIndexUser = Math.floor(Math.random() * 3);
const randomIndexCpu = Math.floor(Math.random() * 3);

const fetchPokemon = () => {
    const promises = [];
    // フシギダネとヒトカゲとゼニガメのidを配列に格納
    pokeArray = new Array(1, 4, 7);
    pokeArray.forEach(pokeId => {
        const url = `https:pokeapi.co/api/v2/pokemon/${pokeId}`;
        promises.push(fetch(url).then((res) => res.json()));     
    });


    Promise.all(promises).then( results => {
        const pokemon = results.map((data) => ({
            name: data.name,
            id: data.id,
            image: data.sprites["front_default"],
            type: data.types.map((type) => type.type.name).join(', ')
        }));
        displayUserPokemon(pokemon);
        displayCpuPokemon(pokemon);
        console.log(pokemon);
    });
};

const displayUserPokemon = async(pokemon) => {
    const pokemonUser = pokemon[randomIndexUser]
    const pokemonHTMLString = `
        <img src="${pokemonUser.image}" />
        <p>${pokemonUser.name}</p>
    `
    pokedexUser.innerHTML = pokemonHTMLString;
};

const displayCpuPokemon = (pokemon) => {
    const pokemonCpu = pokemon[randomIndexCpu]
    const pokemonHTMLString = `
        <img src="${pokemonCpu.image}" />
        <p>${pokemonCpu.name}</p>
    `
    pokedexCpu.innerHTML = pokemonHTMLString;
};

fetchPokemon();

const displayUserHp = document.getElementById('userHP').content
const displayCpuHp = document.getElementById('cpuHP').content

const battle = (displayUserHp, displayCpuHp) => {
    let userHP = displayUserHp;
    let cpuHP = displayCpuHp;
    document.getElementById('userHP').textContent = userHP;
    document.getElementById('cpuHP').textContent  = cpuHP;

    while (cpuHP) {
        let userAttack = Math.floor(Math.random() * 5);
        let cpuAttack = Math.floor(Math.random() * 5);
        cpuHP = cpuHP - userAttack;
        userHP = userHP - cpuAttack;
        document.getElementById('userHP').textContent = userHP;
        document.getElementById('cpuHP').textContent  = cpuHP;
    
        if (userHP > 0){
            if (cpuHP > 0) {
                document.getElementById("text").textContent = "まだ相手の体力は残っているぞ！";
                break
            } else {
                document.getElementById("text").textContent = "やったね！あなたの勝利！";
                break;
            }
        } 
        else if (userHP <= 0 && cpuHP <= 0){
            document.getElementById("text").textContent = "やったね！あなたの勝利！";
            break;
        } 
        else {
            document.getElementById("text").textContent = "残念、あなたの負け...";
            break;
        }
    }




}
