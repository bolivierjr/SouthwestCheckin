import { useState, useEffect } from 'react';

const useWindowDimensions = () => {
  const getDimensions = () => {
    const { innerWidth: width, innerHeight: height } = window;
    return { width, height };
  };

  const [windowDimensions, setWindowDimensions] = useState(getDimensions);

  useEffect(() => {
    const handleResize = () => {
      setWindowDimensions(getDimensions());
    };

    window.addEventListener('resize', handleResize);

    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return windowDimensions;
};

export default useWindowDimensions;
