const axios = require("axios");
const dotenv = require("dotenv");

dotenv.config();

const DEEPSEEK_API_KEY = process.env.DEEPSEEK_API_KEY;

if (!DEEPSEEK_API_KEY) {
    console.error("DEEPSEEK_API_KEY not found in environment variables.");
    process.exit(1);
}

async function makeRequest(
    prompt: string,
    model: string = "deepseek-chat",
    systemRole: string = "You are a helpful assistant.",
    stream: boolean = false
) {
    const baseURL = "https://api.deepseek.com/chat/completions";

    const headers = {
        "Content-Type": "application/json",
        Authorization: `Bearer ${DEEPSEEK_API_KEY}`,
    };

    const payload = {
        model,
        messages: [
            { role: "system", content: systemRole },
            { role: "user", content: prompt },
        ],
        stream,
    };

    try {
        const response = await axios.post(baseURL, payload, { headers });
        console.log("Response:", response.data);
    } catch (error: any) {
        console.error("Request failed:", error.response ? error.response.data : error.message);
    }
}

makeRequest("Hello, how are you?");
