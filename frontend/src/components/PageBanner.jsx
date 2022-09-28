import styles from "../style";

const PgeBanner = (props) => (
  <section id="home" className={`flex md:flex-row flex-col ${styles.paddingY}`}>

    <div className="flex flex-row justify-between items-center w-full">
      <h2 className={styles.heading2}>
        You are in the {props.page} pages!
      </h2>
    </div>
  </section>
);

export default PgeBanner;