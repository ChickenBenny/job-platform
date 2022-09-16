import { Button, Container, Nav, Navbar as NavbarBs } from "react-bootstrap"

export function Navbar() {
    return (
        <NavbarBs bg="dark" variant="dark" expand="lg">
            <Container>
                <NavbarBs.Brand href="/">Hunter X Python</NavbarBs.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/backend">Backend</Nav.Link>
                    <Nav.Link href="/dataEngineer">Data-Engineer</Nav.Link>
                    <Nav.Link href="/dataScientist">Data-Scientist</Nav.Link>
                    <Nav.Link href="/mlEngineer">ML-Engineer</Nav.Link>
                    <Nav.Link href="/qaEngineer">QA-Engineer</Nav.Link>
                </Nav>
                <Button variant="primary" href="https://github.com/ChickenBenny/job-platform">
                    Github Link
                </Button>
            </Container>
        </NavbarBs>
    )
}
