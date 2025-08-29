import express from 'express'
import usersRouter from './routers/UserRouter.js'

export class App {

  constructor() {
    this.app = express()
    this.configureMiddlewares();
    this.configureRouters();
  }

  configureMiddlewares() {
    this.app.use(express.json());
  }
  configureRouters() {
    this.app.use('/v1/users', usersRouter)
  }

  getInstance() {
    return this.app
  }

  listen(port = 9000) {
    this.app.listen(port, () => {
      console.log(`Server listening on: http://localhost:${port}`);
    });
  }
}