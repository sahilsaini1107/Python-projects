import React, { useState } from "react";
import { AppBar, Tab, Tabs, Toolbar, Typography } from "@mui/material";
import LibraryBooksOutlinedIcon from "@mui/icons-material/LibraryBooksOutlined";
import { NavLink } from "react-router-dom";
import { purple, red } from '@mui/material/colors';

const primary = red[500]; // #f44336
const accent = purple['A200']; // #e040fb


const Header = () => {

  const [value, setValue] = useState();

  return (
    <div>
      <AppBar sx={{ backgroundColor: "#212121" }} position="sticky">
        <Toolbar>
          <NavLink to="/" style={{ color: "white" }}>
            <Typography>
              <LibraryBooksOutlinedIcon />
            </Typography>
          </NavLink>
          <Tabs
            sx={{ ml: "auto" }}
            textColor="accent"
            indicatorColor="primary"
            value={value}
            onChange={(e, val) => setValue(val)}
          >
            <Tab LinkComponent={NavLink} to="/add" label="AddProject" />
            <Tab LinkComponent={NavLink} to="/books" label="Allprojects" />
            <Tab LinkComponent={NavLink} to="/about" label="AboutMe" />
          </Tabs>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default Header;