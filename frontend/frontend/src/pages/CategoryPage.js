// src/pages/CategoryPage.js
import React, { useEffect, useState } from "react";
import { Table, Thead, Tbody, Tr, Th, Td } from "@chakra-ui/react";
import { useParams, useNavigate } from "react-router-dom";
import {
  Box,
  Heading,
  VStack,
  Text,
  Flex,
  Button,
  Divider,
  Image,
} from "@chakra-ui/react";
import { ArrowForwardIcon } from "@chakra-ui/icons";

function CategoryPage() {
  const navigate = useNavigate();
  const { category } = useParams();
  const [rankings, setRankings] = useState([]);
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch Top 5 Rankings
        const rankingsRes = await fetch(
          `${process.env.REACT_APP_API_URL}/rankings/${
            category.charAt(0).toUpperCase() + category.slice(1)
          }/?top=5`
        );
        const rankingsData = await rankingsRes.json();
        setRankings(rankingsData);

        // Fetch Recent Matches
        const matchesRes = await fetch(
          `${process.env.REACT_APP_API_URL}/recent-matches/${
            category.charAt(0).toUpperCase() + category.slice(1)
          }/`
        );
        const matchesData = await matchesRes.json();
        setMatches(matchesData); // <- You'll need to define setMatches
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [category]);

  return (
    <Box px={8} py={6} bg="gray.50" minH="100vh">
      {/* Section Header */}
      <Flex
        justify="space-between"
        align="center"
        pl={6}
        pr={8}
        py={4}
        color="gray.800"
      >
        <Heading size="lg">Top 5 Rankings</Heading>
        <Button
          size="md"
          colorScheme="red"
          variant="outline"
          rightIcon={<ArrowForwardIcon />}
          onClick={() => navigate(`/category/${category}/rankings`)}
        >
          View All
        </Button>
      </Flex>

      {/* Rankings Table */}
      <Box px={16} py={4} overflowX="auto">
        {rankings.length > 0 && (
          <Table variant="simple" size="md" bg="white" borderRadius="md">
            <Thead bg="gray.200">
              <Tr>
                <Th textAlign="center">Rank</Th>
                <Th textAlign="center">Player Name</Th>
                <Th textAlign="center">Age</Th>
                <Th textAlign="center">Affiliation</Th>
              </Tr>
            </Thead>
            <Tbody>
              {rankings.map((player) => (
                <Tr key={player.rank}>
                  <Td textAlign="center" fontWeight="bold">
                    #{player.rank}
                  </Td>
                  <Td textAlign="center">{player.player_name}</Td>
                  <Td textAlign="center">{player.age}</Td>
                  <Td textAlign="center">{player.affiliation}</Td>
                </Tr>
              ))}
            </Tbody>
          </Table>
        )}
      </Box>
      <Divider />

      {/* Section Header */}
      <Flex
        justify="space-between"
        align="center"
        pl={6}
        pr={8}
        py={4}
        color="gray.800"
      >
        <Heading size="lg">Recent Matches</Heading>
        <Button
          size="md"
          colorScheme="red"
          variant="outline"
          rightIcon={<ArrowForwardIcon />}
          onClick={() => navigate(`/category/${category}/tournament-matches`)}
        >
          View All
        </Button>
      </Flex>

      {/* Recent Matches */}
      <VStack spacing={4} px={16} py={4} align="center">
        {matches.map((match) => (
          <Box
            key={match.id}
            bg="gray.100"
            p={2}
            borderRadius="md"
            border="1px"
            borderStyle="solid"
            borderColor="gray.200"
            width="100%"
          >
            <Flex
              justify="space-between"
              align="center"
              flexWrap="wrap"
              gap={8}
              textAlign="center"
              px={4}
            >
              {/* Tournament + Date (Left-Pinned) */}
              <Flex
                direction="column"
                align="center"
                minW="140px"
                textAlign="center"
              >
                <Text fontWeight="bold">{match.tournament_name}</Text>
                <Text fontSize="sm" color="gray.500">
                  {match.tournament_date}
                </Text>
              </Flex>

              {/* Center Block: Players + Score */}
              <Flex
                align="center"
                justify="center"
                flex="1"
                gap={12}
                flexWrap="wrap"
                minW="300px"
              >
                {/* Player 1 Info */}
                <Flex gap={3} align="center">
                  <Image
                    src="/images/red_card.png"
                    alt="Red Card"
                    height="25px"
                  />
                  <Text>{match.player_1_red_card_count}</Text>
                  <Image
                    src="/images/yellow_card.png"
                    alt="Yellow Card"
                    height="25px"
                  />
                  <Text>{match.player_1_yellow_card_count}</Text>
                  <Text fontSize="sm" color="gray.500">
                    {match.player_1_affiliation}
                  </Text>
                  <Text fontWeight="semibold">{match.player_1_name}</Text>
                </Flex>

                {/* Score */}
                <Text fontSize="lg" fontWeight="bold">
                  {match.player_1_score} - {match.player_2_score}
                </Text>

                {/* Player 2 Info */}
                <Flex gap={3} align="center">
                  <Text fontWeight="semibold">{match.player_2_name}</Text>
                  <Text fontSize="sm" color="gray.500">
                    {match.player_2_affiliation}
                  </Text>
                  <Image
                    src="/images/red_card.png"
                    alt="Red Card"
                    height="25px"
                  />
                  <Text>{match.player_2_red_card_count}</Text>
                  <Image
                    src="/images/yellow_card.png"
                    alt="Yellow Card"
                    height="25px"
                  />
                  <Text>{match.player_2_yellow_card_count}</Text>
                </Flex>
              </Flex>

              {/* Round (Right-Pinned) */}
              <Box minW="100px" textAlign="right">
                <Text fontSize="sm" color="gray.500" fontStyle="italic">
                  {match.round}
                </Text>
              </Box>
            </Flex>
          </Box>
        ))}
      </VStack>

      {/* Section Header */}
      <Flex
        justify="space-between"
        align="center"
        pl={6}
        pr={8}
        py={4}
        color="gray.800"
      >
        <Heading size="lg">Recent Tournament</Heading>
        <Button
          size="md"
          colorScheme="red"
          variant="outline"
          rightIcon={<ArrowForwardIcon />}
          onClick={() => navigate(`/category/${category}/tournament-matches`)}
        >
          View All
        </Button>
      </Flex>
    </Box>
  );
}

export default CategoryPage;
