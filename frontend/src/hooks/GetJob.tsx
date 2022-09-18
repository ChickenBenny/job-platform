import { useState, useEffect } from "react";

export function GetJob(type: string){
    const [job, setJob] = useState<any>([]);

    useEffect(() => {
        async function getJob() {
            const headers = { 
                'Content-Type': 'application/json',
            };
            const response = await fetch(`https://chickenbenny.com/api/${type}`, {
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