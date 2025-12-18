import { motion } from 'framer-motion';

const Header = () => {
  return (
    <motion.header
      initial={{ opacity: 0, y: -50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="text-center py-8"
    >
      <h1 className="text-6xl font-dancing-script text-white drop-shadow-lg">
        Abigail
      </h1>
      <p className="text-xl text-white/80 mt-2">Hello person</p>
      <p className="text-xl text-white/80 mt-2">The Most Adorable Cat</p>
    </motion.header>
  );
};

export default Header;