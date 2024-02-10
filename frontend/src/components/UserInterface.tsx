import React, { useState, useEffect } from "react";
import axios from "axios";
import CardComponent from "./CardComponent";

interface User {
    id: number;
    name: string;
    email: string;
}

interface UserInterfaceProps {
    backendName: string;
}

const UserInterface: React.FC<UserInterfaceProps> = ({ backendName }) => {
    return (
        <div>
            <h1>{backendName}</h1>
            <CardComponent card={{ id: 1, name: "John Doe", email: "mail" }} />
        </div>
    )
};

export default UserInterface;