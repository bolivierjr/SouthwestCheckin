import { useState, useEffect } from 'react';

/*
  Helper util hook that gets and returns the current
  window dimension sizes using useState and useEffect
  hooks to use the resize event listener on ever re-render.
*/
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
