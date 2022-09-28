import styles from "../style";
import { TbCurrentLocation } from 'react-icons/tb';
import { RiSuitcaseLine } from 'react-icons/ri';
import { RiMoneyDollarCircleFill } from 'react-icons/ri';

export const JobBoard = (props) => {

    return(
        <div>
          {props.data.map(item => (
            <div className={`${styles.flexCenter} ${styles.marginBoxY} ${styles.paddingBoxX} sm:flex-row flex-col bg-black-gradient-2 rounded-[20px] box-shadow`} >
              <div className="flex-1 flex flex-col">
                <h2 className={styles.heading3}><a href={item[0]}>{item[2]}</a></h2>
                <p className={`${styles.paragraph} max-w-[470px] mt-3`}>{item[1]}</p>
                <div className="flex flex-row flex-wrap sm:mt-3 mt-3">{item[3].map(tag => (
                        <h4 className="w-[120px] object-contain cursor-pointer font-poppins font-medium text-[18px] leading-[27px] text-white">
                          {tag} 
                        </h4>
                      ))}</div>
              </div>
              <div className={`flex-1 flex-col `}>
                <div className="flex flex-row">
                  <TbCurrentLocation style={{color: "white", fontSize: "30", marginRight: "10"}}/>
                  <h2 className={styles.headingBox}>Location : {item[5]}</h2>
                </div>
                <div className="flex flex-row">
                  <RiSuitcaseLine style={{color: "white", fontSize: "30", marginRight: "10"}}/>
                    <h2 className={styles.headingBox}>Type : {item[4]}</h2>
                </div>
                <div className="flex flex-row">
                  <RiMoneyDollarCircleFill style={{color: "white", fontSize: "30", marginRight: "10"}}/>
                  <h2 className={styles.headingBox}>Salary : {item[6]}</h2>
                </div>
              </div>
            </div>
          ))}
        </div>
    )
}