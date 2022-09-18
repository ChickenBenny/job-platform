import { useState, useEffect } from "react";

export function GetJob(type: string){
    const [job, setJob] = useState<any>([]);

    useEffect(() => {
        async function getJob() {
            const headers = { 
                'Content-Type': 'application/json',
            };
            const response = await fetch(`http://127.0.0.1/api/${type}`, {
                headers: headers,
                method: 'GET'
            });
            const content = await response.json();
            setJob(content["message"]);
        } 
        getJob();
    }, []);
    return job;
}