const btn = document.getElementById("generateBtn");
const pdfBtn = document.getElementById("analyzePdfBtn");
const downloadBtn = document.getElementById("downloadBtn");

const topic = document.getElementById("topic");
const loading = document.getElementById("loading"); // Kept in HTML but we will rely on agentPanel instead
const output = document.getElementById("output");
const agentPanel = document.getElementById("agentPanel");

// Hide download button initially
downloadBtn.style.display = "none";

// Helper for delays
const delay = ms => new Promise(res => setTimeout(res, ms));

// =============================
// Pipeline Animation Engine
// =============================

async function runPipelineAnimation(type, fetchPromise) {
    const isResearch = type === 'research';
    
    // Configure Task Agent step dynamically
    document.getElementById('name-task').innerText = isResearch ? 'Research Agent' : 'PDF Agent';
    document.getElementById('icon-task').innerText = isResearch ? '🔍' : '📄';
    
    const steps = ['planner', 'task', 'report', 'watsonx', 'complete'];
    
    // Show panel and reset states
    agentPanel.style.display = 'block';
    steps.forEach((step, index) => {
        const el = document.getElementById(`step-${step}`);
        el.className = 'agent-step';
        document.getElementById(`status-${step}`).innerText = 'Waiting...';
        document.getElementById(`badge-${step}`).innerText = 'PENDING';
        
        // Stagger slide-in animation
        setTimeout(() => el.classList.add('visible'), index * 100);
    });
    
    // State helpers
    const setActive = (step, msg) => {
        document.getElementById(`step-${step}`).className = 'agent-step visible active';
        document.getElementById(`status-${step}`).innerText = msg;
        document.getElementById(`badge-${step}`).innerText = 'ACTIVE';
    };
    
    const setDone = (step, msg) => {
        document.getElementById(`step-${step}`).className = 'agent-step visible done';
        document.getElementById(`status-${step}`).innerText = msg;
        document.getElementById(`badge-${step}`).innerText = 'DONE';
    };

    const setError = (step, msg) => {
        document.getElementById(`step-${step}`).className = 'agent-step visible error';
        document.getElementById(`status-${step}`).innerText = msg;
        document.getElementById(`badge-${step}`).innerText = 'ERROR';
    };

    try {
        await delay(400); // Small initial pause
        
        // Step 1: Planner Agent
        setActive('planner', 'Detecting task...');
        await delay(800);
        setDone('planner', `Selected ${isResearch ? 'Research' : 'PDF'} Agent`);
        
        // Step 2: Task Agent
        setActive('task', isResearch ? 'Generating research query...' : 'Extracting PDF text...');
        await delay(800);
        setDone('task', 'Task context prepared');
        
        // Step 3: Report Agent
        setActive('report', 'Preparing report format...');
        await delay(800);
        setDone('report', 'Format ready');
        
        // Step 4: IBM watsonx
        setActive('watsonx', 'Generating insights using IBM watsonx...');
        
        // Wait for the actual API response here
        const response = await fetchPromise;
        const data = await response.json();
        
        if (!response.ok) {
            setError('watsonx', 'API Error');
            throw new Error(data.error || 'Failed to process request with watsonx');
        }
        
        setDone('watsonx', 'Insights generated successfully');
        
        // Step 5: Complete
        setActive('complete', 'Finalizing structured response...');
        await delay(600);
        setDone('complete', 'Complete');
        
        return data;
    } catch (err) {
        // If an error occurs, mark any pending/active steps as error
        steps.forEach(step => {
            const badge = document.getElementById(`badge-${step}`);
            if (badge.innerText === 'ACTIVE' || badge.innerText === 'PENDING') {
                setError(step, 'Failed or Aborted');
            }
        });
        throw err;
    }
}


// =============================
// Generate Research
// =============================

btn.addEventListener("click", async () => {

    const researchTopic = topic.value.trim();

    if (researchTopic === "") {
        alert("Please enter a research topic.");
        return;
    }

    output.innerHTML = "";
    downloadBtn.style.display = "none";
    
    // Hide legacy loading text if it was visible
    if(loading) loading.style.display = "none";

    try {
        // Start the fetch request
        const fetchPromise = fetch("/api/research", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ topic: researchTopic })
        });

        // Run animation concurrently with fetch
        const data = await runPipelineAnimation('research', fetchPromise);

        // Render result
        output.innerHTML = `
            <h2>📄 ${data.structured_report ? data.structured_report.title : "Research Report"}</h2>
            <hr>
            <pre>${data.research}</pre>
        `;

        downloadBtn.style.display = "block";

    } catch (error) {
        output.innerHTML = `
            <h2>Error</h2>
            <p>${error.message || error}</p>
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

    output.innerHTML = "";
    downloadBtn.style.display = "none";

    if(loading) loading.style.display = "none";

    const formData = new FormData();
    formData.append("pdf", file);

    try {
        // Start the fetch request
        const fetchPromise = fetch("/api/analyze_pdf", {
            method: "POST",
            body: formData
        });

        // Run animation concurrently with fetch
        const data = await runPipelineAnimation('pdf', fetchPromise);

        // Render result
        output.innerHTML = `
            <h2>📑 ${data.structured_report ? data.structured_report.title : "PDF Analysis"}</h2>
            <hr>
            <pre>${data.research}</pre>
        `;

        downloadBtn.style.display = "block";

    } catch (error) {
        output.innerHTML = `
            <h2>Error</h2>
            <p>${error.message || error}</p>
        `;
    }

});


// =============================
// Download PDF (Print)
// =============================

downloadBtn.addEventListener("click", () => {
    window.print();
});