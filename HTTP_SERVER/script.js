let count_c = 0;
    document.getElementById('cat').addEventListener('click', async() => {
    cat = document.getElementById('output_cat')
    count_c ++;
    cat.textContent = `Count: ${count_c}`;
    });

    let count_d = 0;
    document.getElementById('dog').addEventListener('click', async() => {
    dog = document.getElementById('output_dog')
    count_d ++;
    dog.textContent = `Count: ${count_d}`;
    });

    let count_p = 0;
    document.getElementById('parrot').addEventListener('click', async() => {
    parrot = document.getElementById('output_parrot')
    count_p ++;
    parrot.textContent = `Count: ${count_p}`;
    });