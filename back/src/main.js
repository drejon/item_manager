import { App } from "./App.js";

const server = new App();

const PORT = process.env.PORT || 9000;

server.listen(PORT);