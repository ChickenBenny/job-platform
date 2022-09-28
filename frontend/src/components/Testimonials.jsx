import styles from "../style";

const Testimonials = (props) => (
  <section id="clients" className={`${styles.paddingBoxY} ${styles.flexCenter} flex-col relative `}>
    <div className="absolute z-[0] w-[60%] h-[60%] -right-[50%] rounded-full blue__gradient bottom-40" />

    <div className="w-full flex justify-between items-center md:flex-row flex-col sm:mb-1 mb-1 relative z-[1]">
      <h2 className={styles.heading2}>
        You are in the {props.page} pages!
      </h2>
    </div>
  </section>
);

export default Testimonials;
