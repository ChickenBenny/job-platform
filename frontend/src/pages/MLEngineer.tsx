import { GetJob } from "../hooks/GetJob"
import { Badge, Container } from "react-bootstrap"
import ListGroup from 'react-bootstrap/ListGroup';

export interface Job {
    length: 8;
    0: string;
    1: string;
    2: string;
    3: string[];
    4: string;
    5: string;
    6: string;
    7: string;
}

export function MLEngineer() {
    const jobItems: Job[] = GetJob("mlEngineer");

    console.log(jobItems)
    return (
        <>
            <Container className="mt-5">
                <ListGroup as="ol">
                    {jobItems.map(item => (
                        <ListGroup.Item
                            as="li"
                            className="d-flex justify-content-between mb-3"
                        >
                            <div className="ms-2 me-auto">
                                <div className="fw-bold ms-3 mt-2"><a style={{ fontSize: '20', color: 'black' }} href={item[0]}>{item[2]}</a></div>
                                <div style={{
                                    display: 'flex'
                                }}>{item[3].map(tag => (
                                    <Badge className="bg-success ms-3 mt-3 mb-2" >{tag}</Badge>
                                ))}</div>
                                <div></div>
                            </div>
                            <div style={{ position: 'absolute', right: '10%' }}>
                                <div><a style={{ fontSize: '14', color: '#6495ED' }}>Type: </a> <a style={{ fontSize: 'bold', color: '#000000' }}>{item[4]}</a></div>
                                <div><a style={{ fontSize: '14', color: '#6495ED' }}>Location: </a> <a style={{ fontSize: 'bold', color: '#000000' }}>{item[5]}</a></div>
                                <div><a style={{ fontSize: '14', color: '#6495ED' }}>Salary: </a> <a style={{ fontSize: 'bold', color: '#000000' }}>{item[6]}</a></div>
                            </div>

                        </ListGroup.Item>
                    ))}
                </ListGroup>
            </Container>

        </>
    )
}