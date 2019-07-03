import React from 'react';
import { Link } from 'react-router-dom';
import { Menu } from 'semantic-ui-react';
import './Header.css';

const Header = ({ path }) => {
  return (
    <Menu pointing secondary>
      <Menu.Item className="brand" name="SW Checkin" color="blue" active />

      <Menu.Menu position="right">
        <Menu.Item
          as={Link}
          to="/"
          name="check-in"
          className="links"
          active={path === '/'}
          color="red"
        />

        <Menu.Item
          as={Link}
          to="/messages"
          name="messages"
          className="links"
          active={path === '/messages'}
          color="red"
        />
      </Menu.Menu>
    </Menu>
  );
};

export default Header;
