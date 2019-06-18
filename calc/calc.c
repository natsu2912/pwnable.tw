unsigned int calc()
{
  int v1; // [esp+18h] [ebp-5A0h]
  int v2[100]; // [esp+1Ch] [ebp-59Ch]
  char s; // [esp+1ACh] [ebp-40Ch]
  unsigned int v4; // [esp+5ACh] [ebp-Ch]

  v4 = __readgsdword(0x14u);
  while ( 1 )
  {
    bzero(&s, 0x400u);
    if ( !get_expr((int)&s, 1024) )
      break;
    init_pool(&v1);
    if ( parse_expr((int)&s, &v1) )
    {
      printf((const char *)&unk_80BF804, v2[v1 - 1]);
      fflush(stdout);
    }
  }
  return __readgsdword(0x14u) ^ v4;
}
