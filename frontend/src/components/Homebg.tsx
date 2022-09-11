import Image from 'react-bootstrap/Image'
import taipeiCity from '../images/TaipeiCity.jpg'

export function Homebg(){
    var textStyle: any = {
        position: 'absolute',
        top: '50%',
        left: '35%',
        color: "white"
    };
    return (
        <div>
            <Image fluid src={taipeiCity} />
            <h1 style={textStyle}>Hunting Your Python Job !</h1>
        </div>
    )
}