const API_URL =
  process.env.NEXT_PUBLIC_API_URL

if (!API_URL) {
  throw new Error(
    "NEXT_PUBLIC_API_URL não definida."
  )
}

export async function apiFetch(
  endpoint: string,
  options?: RequestInit
) {
  const response = await fetch(
    `${API_URL}${endpoint}`,
    {
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...(options?.headers || {})
      }
    }
  )

  if (!response.ok) {
    throw new Error("Erro na requisição")
  }

  return response.json()
}