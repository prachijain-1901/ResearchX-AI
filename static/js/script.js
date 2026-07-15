const btn = document.getElementById("generateBtn");
const pdfBtn = document.getElementById("analyzePdfBtn");
const downloadBtn = document.getElementById("downloadBtn");

const topic = document.getElementById("topic");
const loading = document.getElementById("loading");
const output = document.getElementById("output");

// Hide download button initially
downloadBtn.style.display = "none";


// =============================
// Generate Research
// =============================

btn.addEventListener("click", async () => {

    const researchTopic = topic.value.trim();

    if (researchTopic === "") {
        alert("Please enter a research topic.");
        return;
    }

    loading.style.display = "block";
    output.innerHTML = "";
    downloadBtn.style.display = "none";

    try {

        const response = await fetch("/api/research", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                topic: researchTopic
            })

        });

        const data = await response.json();

        loading.style.display = "none";

        if (!response.ok) {

            output.innerHTML = `
                <h2>Error</h2>
                <p>${data.error}</p>
            `;

            return;
        }

        output.innerHTML = `
            <h2>📄 Research Report</h2>
            <hr>
            <pre>${data.research}</pre>
        `;

        downloadBtn.style.display = "block";

    }

    catch (error) {

        loading.style.display = "none";

        output.innerHTML = `
            <h2>Error</h2>
            <p>${error}</p>
        `;

    }

});


// =============================
// Analyze PDF
// =============================

pdfBtn.addEventListener("click", async () => {

    const file = document.getElementById("pdfFile").files[0];

    if (!file) {

        alert("Please select a PDF.");
        return;

    }

    loading.style.display = "block";
    output.innerHTML = "";
    downloadBtn.style.display = "none";

    const formData = new FormData();
    formData.append("pdf", file);

    try {

        const response = await fetch("/api/analyze_pdf", {

            method: "POST",
            body: formData

        });

        const data = await response.json();

        loading.style.display = "none";

        if (!response.ok) {

            output.innerHTML = `
                <h2>Error</h2>
                <p>${data.error}</p>
            `;

            return;
        }

        output.innerHTML = `
            <h2>📑 PDF Analysis</h2>
            <hr>
            <pre>${data.research}</pre>
        `;

        downloadBtn.style.display = "block";

    }

    catch (error) {

        loading.style.display = "none";

        output.innerHTML = `
            <h2>Error</h2>
            <p>${error}</p>
        `;

    }

});


// =============================
// Download PDF
// =============================

downloadBtn.addEventListener("click", () => {

    window.print();

});