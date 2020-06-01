(()=>{
const comment = document.querySelector(".comment-form")
const unexpectedButton = document.querySelector(".unexpectedButton")
unexpectedButton.addEventListener("click", (e)=>{

    e.preventDefault()
    const content = document.querySelector(".content-xd")
    const itemId = window.location.pathname.split("/")[2]
    const url = comment.getAttribute("action")
    console.log(JSON.stringify({content: content.value, item_id: itemId}))
    fetch(url, {
    headers: {"Content-Type":"application/json"},
    method: "POST",
    body: JSON.stringify({content: content.value, item_id: parseInt(itemId)})
    }
    ).then(r=>r.text()).then(r=>{
    const comment = document.querySelector(".unexpected-comment")
    comment.innerHTML+=r
    })
})

})()