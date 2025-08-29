import { Router } from 'express'

const router = Router()

router.get('/', (req, res) => {
  const users = []

  return res.json(users)
})

export default router