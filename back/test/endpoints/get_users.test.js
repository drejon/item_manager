import request from 'supertest'
import { expect } from 'chai'
import { App } from '../../src/App.js'

const app = new App().getInstance()

describe('GET /v1/users/', function() {
  context('', function() {
    it('shows a list of users', async function() {
      const uri = '/v1/users'

      const res = await request(app)
      .get(uri)

      expect(res.body).to.deep.eq([])
    })
  })
})