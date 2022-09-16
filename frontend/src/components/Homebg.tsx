import Image from 'react-bootstrap/Image'
import { Container } from "react-bootstrap"
import taipeiCity from '../images/TaipeiCity.jpg'

export function Homebg() {

    return (
        <div>
            <Image fluid src={taipeiCity} />
            <Container>
                <h1 style={{
                    position: 'absolute',
                    top: '45%',
                    left: '35%',
                    color: 'white'
                }}>Hunting Your Python Job !</h1>
            </Container>
        </div>
    )
}