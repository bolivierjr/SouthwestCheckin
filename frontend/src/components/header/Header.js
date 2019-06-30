import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu } from 'semantic-ui-react';
import './Header.css';

const Header = () => {
  const [activeItem, setActiveItem] = useState('check-in');

  /*
    Click handler that takes in event target and name
    property of the menu/navbar item and activates it
    by triggering the activateItem state.
  */
  const handleClick = (event, { name }) => setActiveItem(name);

  return (
    <Menu pointing secondary>
      <Menu.Item className="brand" name="SW Checkin" color="blue" active />

      <Menu.Menu position="right">
        <Menu.Item
          as={Link}
          to="/"
          name="check-in"
          className="links"
          active={activeItem === 'check-in'}
          color="red"
          onClick={handleClick}
        />

        <Menu.Item
          as={Link}
          to="/messages"
          name="messages"
          className="links"
          active={activeItem === 'messages'}
          color="red"
          onClick={handleClick}
        />
      </Menu.Menu>
    </Menu>
  );
};

export default Header;
