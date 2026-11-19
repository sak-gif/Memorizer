
const btn = document.getElementById('form')

btn.addEventListener('submit',async (e)=>{
    e.preventDefault()
    const username = document.getElementById('name').value
    const email  = document.getElementById('email').value
    const password = document.getElementById('password').value
    const res = await  fetch("/api/register",{
        method:'POST',
        headers : {"Content-Type" : "application/json" },
        body  : JSON.stringify({username,email,password})

    }
    )
    const data = await res.json()
    console.log(data)

})