async function generateBlog() {

    const url = document.getElementById("videoUrl").value;

    const response = await fetch("http://127.0.0.1:8000/generate-blog", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    });

    const data = await response.json();

    document.getElementById("result").innerText = data.blog;
}