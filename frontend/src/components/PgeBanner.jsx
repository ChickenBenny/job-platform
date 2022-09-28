import styles from "../style";

const PgeBanner = (props) => (
  <section id="clients" className={`${styles.paddingBoxY} ${styles.flexCenter} flex-col relative `}>

    <div className="w-full flex justify-between items-center md:flex-row flex-col sm:mb-1 mb-1 relative z-[1]">
      <h2 className={styles.heading2}>
        You are in the {props.page} pages!
      </h2>
    </div>
  </section>
);

export default PgeBanner;
